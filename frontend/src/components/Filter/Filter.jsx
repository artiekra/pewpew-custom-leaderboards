/* eslint-disable react/prop-types */
import './Filter.css'

const Filter = ({ onSubmit }) => {
    const handleSubmit = (event) => {
        event.preventDefault();
        const form = event.target;

        const dateFrom = new Date(form.date_from.value);
        const timestampStart = Math.floor(dateFrom.getTime() / 1000);

        const dateTo = new Date(form.date_to.value);
        const timestampEnd = Math.floor(dateTo.getTime() / 1000);

        const era = form.era.value;

        onSubmit({ timestampStart, timestampEnd, era });
    };

    return (
        <div className="filter">
            <form className="filter-form" onSubmit={handleSubmit}>
                <label htmlFor="date_from">Date from:</label>
                <input type="date" id="date_from" name="date_from" required />

                <label htmlFor="date_to">Date to:</label>
                <input type="date" id="date_to" name="date_to" required />

                <label htmlFor="era">Era:</label>
                <select id="era" name="era" required defaultValue={2}>
                    <option value="0">0</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                </select>

                <button type="submit" id='submitBtn'>
                    <svg width="140" height="50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 50" preserveAspectRatio="xMidYMid meet">
                        <rect x="5" y="40" width="5" height="5" fill="none" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                        <rect x="180" y="5" width="5" height="5" fill="none" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                        <line x1="1" y1="12" x2="12" y2="1" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                        <line x1="179" y1="49" x2="190" y2="37" stroke="rgb(19, 65, 150)" strokeWidth="2" />
                        <polygon points="20,0 190,0 190,30 172,50 0,50 0,40 0,20" fill="none" stroke="rgb(19, 65, 150)" strokeWidth="3"/>
                        <text className='text' x="50%" y="50%" textAnchor="middle" fill="white" dy=".3em" fontSize="27">Apply</text>
                    </svg>
                </button>
            </form>
        </div>
    );
};

export default Filter;
