import React from 'react';

import MoCover from './MoCover';

import '../res/lo-mo-cover.less';


export default class LoMoCover extends React.Component {
  handleMoClick(movie) {
    if (typeof this.props.onMoClick === 'function') {
      this.props.onMoClick(movie);
    }
  }

  render() {
    return (
      <ul className="cnm-lo-mo-cover">
        {
          (this.props.data && this.props.data.length) ?
          (this.props.data.map(movie => (
            <li key={movie.id} onClick={() => this.handleMoClick(movie)}>
              <MoCover data={movie} />
            </li>
          )))
          :
          <li className="empty">(无)</li>
        }
      </ul>
    );
  }
}
