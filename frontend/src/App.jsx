import { useState, useEffect } from 'react';
import Table from './components/Table/Table'
import { fetchData } from './services/api';

const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchDataAndLog = async () => {
      try {
        const result = await fetchData();
        console.log('JSON data:', result);
        setData(result);
      } catch (error) {
        console.error('Error fetching and logging data:', error);
      }
    };

    fetchDataAndLog();
  }, []);

  return (
    <div>
      <Table data={data} />
    </div>
  );
};

export default App;