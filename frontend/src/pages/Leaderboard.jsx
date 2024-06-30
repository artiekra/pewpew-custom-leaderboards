import { useState, useEffect } from 'react'
import Table from '../components/Table/Table'
import Filter from '../components/Filter/Filter'
import { fetchData } from '../services/api'

const Leaderboard = () => {
    const [data, setData] = useState([]);
    const [page, setPage] = useState(0);
    const [filters, setFilters] = useState({ timestampStart: null, timestampEnd: null, era: 2 });

    useEffect(() => {
        const fetchDataAndLog = async () => {
            try {
                const { timestampStart, timestampEnd, era } = filters;
                let url = `http://localhost:8000/v1/scores/get_scores/?page=${page}&limit=45`;
                if (timestampStart && timestampEnd && era !== null) {
                    url += `&timestamp_start=${timestampStart}&timestamp_end=${timestampEnd}&era=${era}`;
                }
                const result = await fetchData(url);
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
    }, [page, filters]);

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
    }, []);

    const handleFilterSubmit = ({ timestampStart, timestampEnd, era }) => {
        setFilters({ timestampStart, timestampEnd, era });
        setPage(0);
    };

    return (
        <div>
            <h1>Leaderboard</h1>
            <Filter onSubmit={handleFilterSubmit} />
            <Table data={data} />
        </div>
    );
};

export default Leaderboard;
