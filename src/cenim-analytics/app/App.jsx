import React from 'react';
import { render } from 'react-dom';
import ReactCSSTransitionGroup from 'react-addons-css-transition-group';

import { loadClusters } from '../api';

import '../index.html';
import '../res/app.less';


export default class App extends React.Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() {
    this.initialLoad();
  }

  async initialLoad() {
    const clusters = loadClusters();
  }

  render() {
    return (
      <div className="cnm-analysis-app">
        <h1>cnm-analysis-app</h1>
      </div>
    );
  }
}


render(
  <App />,
  document.getElementById('cnm-root')
);
