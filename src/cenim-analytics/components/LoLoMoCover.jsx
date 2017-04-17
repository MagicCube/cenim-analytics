import React from 'react';

import LoMoCover from './LoMoCover';

import '../res/lo-lo-mo-cover.less';


export default class LoLoMoCover extends React.Component {
  handleMoClick(movie) {
    if (typeof this.props.onMoClick === 'function') {
      this.props.onMoClick(movie);
    }
  }

  render() {
    return (
      <ul className="cnm-lo-lo-mo-cover">
        {this.props.data.map((cluster, i) => (
          <li key={`cluster-${i}`}>
            <div>{cluster._tags.join(', ')}</div>
            <LoMoCover data={cluster.movies} onMoClick={movie => this.handleMoClick(movie)} />
          </li>
        ))}
      </ul>
    );
  }
}
