import React from 'react';
import { Drawer, Button, Row, Col } from 'antd';
import { MenuUnfoldOutlined } from '@ant-design/icons';

import LeftMenu from './LeftMenu';
import RightMenu from './RightMenu';
import './NavBar.css';
import logo from '../../assets/img/logo.png';

function Navbar() {
  const [visible, setVisible] = React.useState(false);

  const showDrawer = () => {
    setVisible(true);
  };

  const onClose = () => {
    setVisible(false);
  };

  return (
    <Row align="middle">
      <Col span={14} offset={5}>
        <nav className="navbar">
          <div className="navbar-logo">
            <Button type="link" href="#">
              <img
                style={{ maxWidth: '100%', height: 'auto' }}
                src={logo}
                alt="Graditude Logo"
              />
            </Button>
          </div>
          <div className="navbar-container">
            <div className="navbar-left">
              <LeftMenu mode="horizontal" />
            </div>
            <div className="navbar-right">
              <RightMenu mode="horizontal" />
            </div>
            <Button
              className="navbar-mobile-button"
              type="primary"
              onClick={showDrawer}
            >
              <MenuUnfoldOutlined />
            </Button>
            <Drawer
              title="Basic Drawer"
              placement="right"
              className="navbar-drawer"
              closable={false}
              onClose={onClose}
              visible={visible}
            >
              <LeftMenu mode="inline" />
              <RightMenu mode="inline" />
            </Drawer>
          </div>
        </nav>
      </Col>
    </Row>
  );
}

export default Navbar;
