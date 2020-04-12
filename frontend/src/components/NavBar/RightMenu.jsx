import React from 'react';
import PropTypes from 'prop-types';
import { Menu, Button } from 'antd';

function RightMenu({ mode }) {
  return (
    <Menu mode={mode}>
      <Menu.Item key="signin">
        <Button type="primary">Sign In</Button>
      </Menu.Item>
    </Menu>
  );
}

RightMenu.propTypes = {
  mode: PropTypes.string.isRequired,
};

export default RightMenu;
