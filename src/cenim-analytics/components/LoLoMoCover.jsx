import React from 'react';

import LoMoCover from './LoMoCover';

import '../res/lo-lo-mo-cover.less';


export default class LoLoMoCover extends React.Component {
  render() {
    return (
      <ul className="cnm-lo-lo-mo-cover">
        {this.props.data.map((cluster, i) => (
          <li key={`cluster-${i}`}>
            <div>{cluster._tags.join(', ')}</div>
            <LoMoCover data={cluster.movies} />
          </li>
        ))}
      </ul>
    );
  }
}
