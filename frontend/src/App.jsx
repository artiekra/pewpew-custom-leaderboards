import { useState, useEffect } from 'react';
import Table from './components/Table/Table';
import { fetchData } from './services/api';

const App = () => {
  const [data, setData] = useState([]);
  const [page, setPage] = useState(0);

  useEffect(() => {
    const fetchDataAndLog = async () => {
      try {
        const result = await fetchData(`http://localhost:8000/v1/scores/get_scores/?page=${page}&limit=45`);
        if (page === 0) {
          setData(result);
        } else {
          setData(prevData => [...prevData, ...result]);
        }
      } catch (error) {
        console.error('Error fetching and logging data:', error);
      }
    };

    fetchDataAndLog();
  }, [page]);

  useEffect(() => {
    let fetching = false;

    const handleScroll = () => {
      const windowHeight = window.innerHeight;
      const documentHeight = document.documentElement.scrollHeight;
      const scrollTop = window.scrollY || document.body.scrollTop + (document.documentElement && document.documentElement.scrollTop || 0);
      if (!fetching && documentHeight - (scrollTop + windowHeight) < 20) {
        fetching = true;
        setPage(prevPage => prevPage + 1);
      }
    };

    const onScroll = () => {
      handleScroll();
      fetching = false;
    };

    window.addEventListener('scroll', onScroll);

    return () => {
      window.removeEventListener('scroll', onScroll);
    };
  }, [page]);

  return (
    <div>
      <Table data={data} />
    </div>
  );
};

export default App;
