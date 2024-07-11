import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { requestAPI } from './handler';

/**
 * Initialization data for the cscienv_nbgrader_exchange extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'cscienv_nbgrader_exchange:plugin',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('JupyterLab extension cscienv_nbgrader_exchange is activated!');

    requestAPI<any>('get_example')
      .then(data => {
        console.log(data);
      })
      .catch(reason => {
        console.error(
          `The cscienv_nbgrader_exchange server extension appears to be missing.\n${reason}`
        );
      });
  }
};

export default plugin;
