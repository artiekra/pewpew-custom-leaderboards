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

                <input type="submit" value="Apply" />
            </form>
        </div>
    );
};

export default Filter;
