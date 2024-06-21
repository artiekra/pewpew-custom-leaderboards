/* eslint-disable react/prop-types */
import './Table.css'

const Table = ({ data }) => {
    if (!Array.isArray(data)) {
        return <p>Loading...</p>;
    }

    const convertTimestampToUserTimezone = (timestamp) => {
        const date = new Date(timestamp * 1000);
        return date.toLocaleString('ja-JP', {
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false
        }).replace(',', '');
    };

    return (
        <div className='table'>
            <table>
                <thead>
                    <tr>
                        <th>id</th>
                        <th>timestamp</th>
                        <th>era</th>
                        <th>username1</th>
                        <th>username2</th>
                        <th>level</th>
                        <th>score</th>
                        <th>country</th>
                        <th>platform</th>
                        <th>mode</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((item) => (
                        <tr key={item.id}>
                            <td>{item.id}</td>
                            <td>{convertTimestampToUserTimezone(item.timestamp)}</td>
                            <td>{item.era}</td>
                            <td>{item.username1}</td>
                            <td>{item.username2}</td>
                            <td>{item.level}</td>
                            <td>{item.score}</td>
                            <td>{item.country}</td>
                            <td>{item.platform}</td>
                            <td>{item.mode}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Table;
