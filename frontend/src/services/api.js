export const fetchData = async (baseURL) => {
    try {
        const response = await fetch(baseURL, {
            method: 'GET',
            headers : {
                'Content-Type': 'application/json'
            }
        });
        
        if(!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const data = await response.json();
        return data["result"];
    } catch (error) {
        console.log('Error fetching data:', error);
        throw error;
    }
};
