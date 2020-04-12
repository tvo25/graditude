import React from 'react';
import { Row, Col, Button } from 'antd';

const styles = {
  container: {
    height: '544px',
    background:
      'linear-gradient(180deg, rgba(255, 255, 255, 1) 0%, rgba(28, 93, 132, 0.06993090204831931) 100%)',
  },
  heroTitle: {
    fontSize: '2.5rem',
    fontWeight: 'bold',
  },
};

function Hero() {
  return (
    <Row style={styles.container} type="flex" align="middle">
      <Col span={10} offset={6}>
        <h1 style={styles.heroTitle}>
          It only takes a little bit of Graditude.
        </h1>
        <p>Graditude aims to optimize your job hunt with just a few clicks.</p>

        <Button type="primary">Ready to elevate your search?</Button>
      </Col>
    </Row>
  );
}

export default Hero;
