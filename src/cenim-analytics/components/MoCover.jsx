import React from 'react';

import '../res/mo-cover.less';


export default class MoCover extends React.Component {
  render() {
    return (
      <div className="cnm-mo-cover" style={{ backgroundImage: `url(${this.props.data.img})` }}>
        { this.props.displayTitle ? <div className="title">{this.props.data.title}</div> : null }
      </div>
    );
  }
}
