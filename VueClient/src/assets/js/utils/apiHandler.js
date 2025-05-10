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

    //  Ensure that the payload is an object
    if (!payload)
    {
        console.log("No payload provided, using default value.", path, payload);
        await axios.get(path).then((res) => 
        {
            response.data = res.data.data;
            response.Total = res.data.page;

            console.log("Response.js :", response);
        }).catch((err) => 
        {
            throw new Error("[Error] Response.js :" ,err);
        });
    }
    else
    {
        await axios.post(path, payload).then((res) => 
        {
            response.data = res.data.data;
            response.Total = res.data.page;

            console.log("with payload, Response.js :", response);
        }).catch((err) => 
        {
            throw new Error("[Error] Response.js :" ,err);
        });
    }
    return response;

}
export async function clearResponse(path, payload = null)
{
    response =  reactive({
        Total: null,
        data: null,
    });

}