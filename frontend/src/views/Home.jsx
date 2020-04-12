import React from 'react';
import { Row, Col, Typography } from 'antd';
import Hero from '../components/Hero';

import teamImg from '../assets/img/teamwork.svg';
import cloudImg from '../assets/img/cloud-computing.svg';
import yogaImg from '../assets/img/yoga.svg';

const styles = {
  img: { height: '128px', width: '128px' },
  promoCaption: { fontWeight: 'bold', fontSize: '14px' },
};

function Home() {
  return (
    <div>
      <div>
        <Hero />
      </div>
      <div style={styles.promoContainer}>
        <Row type="flex" align="middle">
          <Col xs={24} sm={24} md={8} lg={8} xl={8}>
            <img style={styles.img} src={teamImg} alt="team"></img>
            <p style={styles.promoCaption}>Stay Motivated</p>
            <p>
              Job hunting for new graduates can be tough. Graditude&apos;s
              mission is to encourage the growth of the next generation of
              professionals.
            </p>
          </Col>
          <Col xs={24} sm={24} md={8} lg={8} xl={8}>
            <img style={styles.img} src={cloudImg} alt="cloud"></img>
            <p style={styles.promoCaption}>Searching, made simple</p>
            <p>
              Browse a simple, centralized database curated using Indeed.
              Graditude&apos;s listings are updated twice an hour, every hour.
            </p>
          </Col>
          <Col xs={24} sm={24} md={8} lg={8} xl={8}>
            <img style={styles.img} src={yogaImg} alt="stress-free"></img>
            <p style={styles.promoCaption}>Ad-free, stress-free</p>
            <p>
              Graditude makes job-hunting stress-free by filtering out ads and
              displaying posts tabularly. The fewer clicks are made, the more
              efficient searching becomes.
            </p>
          </Col>
        </Row>
      </div>
    </div>
  );
}

export default Home;
