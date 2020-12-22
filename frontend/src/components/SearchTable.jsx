import { Button, Table } from 'antd';
import axios from 'axios';
import React from 'react';
import { useAsync } from 'react-async';

const fetchPosts = async () => {
  return axios
    .get('/api/v1/jobs/posts/')
    .then((res) => (res.statusText === 'OK' ? res : Promise.reject(res)))
    .then((res) => res);
};

function SearchTable() {
  const { data, isLoading } = useAsync(fetchPosts);

  if (isLoading) {
    return 'Is Loading';
  }

  const tableConfig = {
    size: 'small',
    loading: isLoading,
    pagination: { position: ['bottomCenter'], showSizeChanger: true },
    hasData: true,
    defaultSortOrder: 'descend',
  };

  const columns = [
    {
      title: 'Date Posted',
      dataIndex: 'date_posted',
      width: 100,
    },
    {
      title: 'Title',
      dataIndex: 'title',
    },
    {
      title: 'Company',
      dataIndex: 'company',
    },
    {
      title: 'Location',
      dataIndex: 'location',
    },
    {
      title: 'Description',
      dataIndex: 'description',
      width: 400,
    },
    {
      title: 'Source',
      dataIndex: 'link',
      render: (link) => (
        <Button type="link" href={link} target="_blank">
          Link
        </Button>
      ),
    },
    {
      title: 'Sponsored',
      dataIndex: 'sponsored',
      render: (sponsored) => (sponsored ? 'Yes' : 'No'),
    },
  ];

  return (
    <div>
      <Table
        // eslint-disable-next-line react/jsx-props-no-spreading
        {...tableConfig}
        columns={columns}
        dataSource={tableConfig.hasData ? data.data : null}
        rowKey="id"
        scroll={{ y: 700 }}
      />
    </div>
  );
}

export default SearchTable;
