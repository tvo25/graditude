import React from 'react';
import PropTypes from 'prop-types';
import { Menu, Button } from 'antd';

const styles = {
  buttonLink: { color: 'black' },
};

function LeftMenu({ mode }) {
  return (
    <Menu mode={mode}>
      <Menu.Item key="about">
        <Button type="link" style={styles.buttonLink}>
          About
        </Button>
      </Menu.Item>
      <Menu.Item key="careers">
        <Button type="link" style={styles.buttonLink}>
          Careers
        </Button>
      </Menu.Item>
    </Menu>
  );
}

LeftMenu.propTypes = {
  mode: PropTypes.string.isRequired,
};

export default LeftMenu;
