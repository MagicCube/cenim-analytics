import React from 'react';
import { render } from 'react-dom';
import ReactCSSTransitionGroup from 'react-addons-css-transition-group';

import { loadClusters } from '../api';
import LoLoMoCover from '../components/LoLoMoCover';
import LoMoCover from '../components/LoMoCover';

import '../index.html';
import '../res/app.less';


export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      clusters: [],
      selectedMovies: [],
      recommendedMovies: []
    };
  }

  componentDidMount() {
    this.initialLoad();
  }

  async initialLoad() {
    const clusters = await loadClusters();
    this.setState({ clusters });
  }

  handleMoClick(movie) {
    if (!this.state.selectedMovies.includes(movie)) {
      movie.selected = true;
      this.state.selectedMovies.push(movie);
    } else {
      movie.selected = false;
      const index = this.state.selectedMovies.indexOf(movie);
      this.state.selectedMovies.splice(index, 1);
    }
    this.forceUpdate();
  }

  render() {
    return (
      <div className="cnm-analysis-app">
        <section className="all">
          <header>
            <h3>所有影片</h3>
          </header>
          <main>
            <LoLoMoCover data={this.state.clusters} displayCheck={true} onMoClick={movie => this.handleMoClick(movie)} />
          </main>
        </section>

        <section className="recommendations">
          <div>
            <h3>选中的影片 (<span>{this.state.selectedMovies.length}</span> 部)</h3>
            <LoMoCover data={this.state.selectedMovies} small={true} displayTitle={false} onMoClick={movie => this.handleMoClick(movie)} />
          </div>
          <div>
            <h3>推荐的影片 (<span>{this.state.recommendedMovies.length}</span> 部)</h3>
            <LoMoCover data={this.state.recommendedMovies} onMoClick={movie => this.handleMoClick(movie)} />
          </div>
        </section>
      </div>
    );
  }
}


render(
  <App />,
  document.getElementById('cnm-root')
);
