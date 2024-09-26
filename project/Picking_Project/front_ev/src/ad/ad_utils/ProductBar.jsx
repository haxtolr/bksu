import React, { useState, useEffect } from 'react';
import { BarChart } from '@mui/x-charts/BarChart';

const InventoryChart = ({ products }) => {
  const [chartData, setChartData] = useState([]);

  useEffect(() => {
    // products 배열에서 product_name을 y축으로, quantity를 x축으로 하는 데이터로 가공
    const chartData = products.map((product, index) => ({
      y: product.product_name,
      x: product.quantity,
      color: getRandomColor(index) // 랜덤 색상 생성
    }));
    // 그래프에 데이터 설정
    setChartData(chartData);
  }, [products]);

  const valueFormatter = value => `${value} 개`; // 값 형식 변환

  const getRandomColor = (index) => {
    const colors = [
      '#FF5733', '#33FF57', '#5733FF', '#FF33A8', '#33FFFF', // 색상 배열
      '#33FFC5', '#FF33F9', '#33A8FF', '#FFA833', '#FFFF33'
    ];
    return colors[index % colors.length]; // 인덱스에 따라 색상 선택
  };

  const chartSetting = {
    width: 500, // 차트의 가로 크기
    height: 400, // 차트의 세로 크기
  };

  return (
    <BarChart
      dataset={chartData}
      yAxis={[{ scaleType: 'band', dataKey: 'y' }]} // y축으로 상품명 사용
      series={[{ dataKey: 'x', label: '재고', valueFormatter, colorKey: 'color' }]} // x축으로 수량 사용
      layout="horizontal"
      {...chartSetting}
    />
  );
};

export default InventoryChart;
