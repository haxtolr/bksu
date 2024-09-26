import * as React from 'react';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import { PieChart, pieArcLabelClasses } from '@mui/x-charts/PieChart';

const pieParams = { height: 400, margin: { right: 30 } };
const palette = ['red', 'blue', 'green', 'yellow'];

const data = [
  { value: 11, label: 'A 지역' },
  { value: 35, label: 'B 지역' },
  { value: 19, label: 'C 지역' },
  { value: 23, label: 'D 지역' },
  
];
export default function PieColor() {
  return (
    <Stack direction="row" width="100%" textAlign="center" spacing={4}>
      <Box flexGrow={1}>
        <Typography></Typography>
        <PieChart
          series={[
            {
              data: data,
              arcLabel: (item) => `${item.label} (${item.value})`,
              arcLabelMinAngle: 45,
            },
          ]}
          sx={{
            [`& .${pieArcLabelClasses.root}`]: {
              fill: 'white',
              fontWeight: 'bold',
            },
          }}
          {...pieParams}
        />
      </Box>
    </Stack>
  );
}
