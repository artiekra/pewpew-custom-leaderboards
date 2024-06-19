/* eslint-disable react/prop-types */
import './Table.css';

const Table = ({ data }) => {
    if (!Array.isArray(data)) {
        return <p>Loading...</p>;
    }

    return (
        <table>
        <caption>Score table of users</caption>
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
                <td>{item.timestamp}</td>
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
    );
};

export default Table;