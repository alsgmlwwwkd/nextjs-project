// typescript로 만든 component

import "./FredSeriesListView.scss";

import { AppstoreOutlined, MailOutlined, SettingOutlined } from '@ant-design/icons';

import { Menu } from 'antd';

export default function FredSeriesListView() {
    const handleClick = (e: any) => {
        console.log('click ', e);
      };
    
    return (
        <div className="fred-series-list-view">
            <Menu
                onClick={handleClick}
                style={{ width: 256 }}
                defaultSelectedKeys={['1']}
                defaultOpenKeys={['sub1']}
                mode="inline"
            ></Menu>
        </div>
    );    
}