import * as React from 'react';
import { BarChart, BarElement } from '@mui/x-charts';

export default function ChartsOverviewDemo() {
  // 각 바의 색상을 정의합니다.
  const barColors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1'];

  return (
    <BarChart
      series={[
        { 
          data: [3, 20, 40, 30],
        },
      ]}
      height={290}
      xAxis={[{ data: ['A 지역', 'B 지역', 'C 지역', 'D 지역'], scaleType: 'band' }]}
      margin={{ top: 10, bottom: 30, left: 40, right: 10 }}
      barComponent={(props) => (
        <BarElement {...props} color={barColors[props.index]} />
      )}
    />
  );
}
