import glob
import nbgrader.exchange.default.collect as collect
from nbgrader.api import Gradebook, MissingEntry
from nbgrader.utils import check_mode
import os

class ExchangeCollect(collect.ExchangeCollect):
    def _path_to_record(self, path):
        """
        Wraps the default _path_to_record function adjusting the 'filename' key
        to prepend the student specific folder.
        """
        record = super()._path_to_record(path)
        record['filename'] = os.path.join(record['username'], record['filename'])
        return record

    def init_src(self):
        if self.coursedir.course_id == '':
            self.fail("No course id specified. Re-run with --course flag.")

        self.course_path = os.path.join(self.root, self.coursedir.course_id)
        self.inbound_path = os.path.join(self.course_path, 'inbound')
        if not os.path.isdir(self.inbound_path):
            self.fail("Course not found: {}".format(self.inbound_path))
        if not check_mode(self.inbound_path, read=True, execute=True):
            self.fail("You don't have read permissions for the directory: {}".format(self.inbound_path))
        student_id = self.coursedir.student_id if self.coursedir.student_id else '*'
        pattern = os.path.join(self.inbound_path, '{}'.format(student_id), '{}+{}+*'.format(student_id, self.coursedir.assignment_id))
        records = [self._path_to_record(f) for f in glob.glob(pattern)]
        usergroups = collect.groupby(records, lambda item: item['username'])

        with Gradebook(self.coursedir.db_url, self.coursedir.course_id) as gb:
            try:
                assignment = gb.find_assignment(self.coursedir.assignment_id)
                self.duedate = assignment.duedate
            except MissingEntry:
                self.duedate = None
        if self.duedate is None or not self.before_duedate:
            self.src_records = [self._sort_by_timestamp(v)[0] for v in usergroups.values()]
        else:
            self.src_records = []
            for v in usergroups.values():
                records = self._sort_by_timestamp(v)
                records_before_duedate = [record for record in records if record['timestamp'] <= self.duedate]
                if records_before_duedate:
                    self.src_records.append(records_before_duedate[0])
                else:
                    self.src_records.append(records[0])
