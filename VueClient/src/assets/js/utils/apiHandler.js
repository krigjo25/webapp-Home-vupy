//  Server API response handler

//  Importing dependencies
import axios from 'axios';
import { reactive } from 'vue';

const response =  reactive({
    Total: null,
    data: null,
});

export async function FetchApiResponse(path, payload = null)
{

    await axios.get(path, payload).then((res) => 
    {
        response.data = res.data.data;
        response.Total = res.data.page;

        console.log("Response.js :", response);
    }).catch((err) => 
    {
        console.error("[Error] Response.js :" ,err);
    });

    return response;

}