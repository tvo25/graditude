import React from 'react';
import { Row, Col, Typography } from 'antd';
import Hero from '../components/Hero';

import teamImg from '../assets/img/teamwork.svg';
import cloudImg from '../assets/img/cloud-computing.svg';
import yogaImg from '../assets/img/yoga.svg';

const styles = {
  img: { height: '128px', width: '128px' },
  promoContainer: { marginTop: '3em' },
  promoTitle: { fontWeight: 'bold', fontSize: '1rem' },
  promoCaption: { fontSize: '1rem' },
};

function Home() {
  return (
    <div>
      <div>
        <Hero />
      </div>
      <div style={styles.promoContainer}>
        <Row type="flex" align="middle">
          <Col
            xs={24}
            sm={{ span: 20, offset: 2 }}
            md={{ span: 4, offset: 4 }}
            lg={{ span: 4, offset: 4 }}
            xl={{ span: 4, offset: 4 }}
            data-aos="zoom-in"
          >
            <img style={styles.img} src={teamImg} alt="team"></img>
            <p style={styles.promoTitle}>Stay Motivated</p>
            <p style={styles.promoCaption}>
              Graditude&apos;s mission is to encourage the growth of the next
              generation of professionals.
            </p>
          </Col>
          <Col
            xs={24}
            sm={{ span: 20, offset: 2 }}
            md={{ span: 4, offset: 2 }}
            lg={{ span: 4, offset: 2 }}
            xl={{ span: 4, offset: 2 }}
            data-aos="zoom-in"
          >
            <img style={styles.img} src={cloudImg} alt="cloud"></img>
            <p style={styles.promoTitle}>Searching, made simple</p>
            <p style={styles.promoCaption}>
              Browse a simple, centralized database curated using Indeed.
              Graditude&apos;s listings are updated twice an hour, every hour.
            </p>
          </Col>
          <Col
            xs={24}
            sm={{ span: 20, offset: 2 }}
            md={{ span: 4, offset: 2 }}
            lg={{ span: 4, offset: 2 }}
            xl={{ span: 4, offset: 2 }}
            data-aos="zoom-in"
          >
            <img style={styles.img} src={yogaImg} alt="stress-free"></img>
            <p style={styles.promoTitle}>Ad-free, stress-free</p>
            <p style={styles.promoCaption}>
              Graditude makes job-hunting stress-free by being ad-free and easy
              to navigate. The fewer clicks are made, the more efficient
              searching becomes.
            </p>
          </Col>
        </Row>
      </div>
    </div>
  );
}

export default Home;
