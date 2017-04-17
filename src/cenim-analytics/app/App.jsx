import React from 'react';
import { render } from 'react-dom';
import ReactCSSTransitionGroup from 'react-addons-css-transition-group';

import { loadClusters } from '../api';
import LoLoMoCover from '../components/LoLoMoCover';

import '../index.html';
import '../res/app.less';


export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      clusters: []
    };
  }

  componentDidMount() {
    this.initialLoad();
  }

  async initialLoad() {
    const clusters = await loadClusters();
    this.setState({ clusters });
  }

  render() {
    return (
      <div className="cnm-analysis-app">
        <section className="all">
          <header>
            <h3>所有影片</h3>
          </header>
          <main>
            <LoLoMoCover data={this.state.clusters} />
          </main>
        </section>

        <section className="recommendations">
          <header>
            <h3>推荐的影片</h3>
          </header>
          <main>
          </main>
        </section>
      </div>
    );
  }
}


render(
  <App />,
  document.getElementById('cnm-root')
);
