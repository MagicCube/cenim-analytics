import React from 'react';

import MoCover from './MoCover';

import '../res/lo-mo-cover.less';


export default class LoMoCover extends React.Component {
  static defaultProps = {
    displayTitle: true,
    displayCheck: false
  }

  handleMoClick(movie) {
    if (typeof this.props.onMoClick === 'function') {
      this.props.onMoClick(movie);
    }
  }

  render() {
    return (
      <ul className={this.props.small ? "cnm-lo-mo-cover small" : "cnm-lo-mo-cover"}>
        {
          (this.props.data && this.props.data.length) ?
          (this.props.data.map(movie => (
            <li key={movie.id} className={this.props.displayCheck && movie.selected ? 'selected' : null} onClick={() => this.handleMoClick(movie)}>
              <MoCover data={movie} displayTitle={this.props.displayTitle} />
              <div className='check' />
            </li>
          )))
          :
          <li className="empty">(无)</li>
        }
      </ul>
    );
  }
}
