import React from 'react';

import MoCover from './MoCover';

import '../res/lo-mo-cover.less';


export default class LoMoCover extends React.Component {
  render() {
    return (
      <ul className="cnm-lo-mo-cover">
        {this.props.data.map(movie => (
          <li key={movie.id}>
            <MoCover data={movie} />
          </li>
        ))}
      </ul>
    );
  }
}
