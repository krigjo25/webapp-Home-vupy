import axios from 'axios';
import { reactive } from 'vue';

export const pfolio =  reactive({
    Total: 0,
    data: [],
});

export async function Response(path, payload = null)
{
    const response = reactive({data: null});

    if (!payload)
    {
        await axios.get(path)
        .then((res) => 
        {
            response.data = res.data.data;
            response.Total = res.data.page;

            console.log("Response.js :", response);
        })
        .catch((err) => 
        {
            console.error("[Error] Response.js :" ,err);
        });
    }
    else
    {
        await axios.get(path, payload)
        .then((res) => 
        {
            response.data = res.data.data;
            response.Total = res.data.page;

            console.log("Response.js :", response);
        })
        .catch((err) => 
        {
            console.error("[Error] Response.js :" ,err);
        });
    }

    return response;

}