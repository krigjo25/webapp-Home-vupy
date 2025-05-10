import axios from 'axios';
import { reactive } from 'vue';

export const pfolio =  reactive({
    Total: 0,
    data: [],
});

export async function Response(path, payload = null)
{

    const response = reactive(
        {
            Total: 0,
            data: null,

        });

    if (!payload)
    {
        await axios.get(path)
        .then((res) => 
        {
            response.Total = res.data.page;
            response.data = res.data.data;
        })
        .catch((err) => 
        {
            console.log(err);
        });
    }
    else
    {
        await axios.get(path, payload)
        .then((res) => 
        {
            response.Total = res.data.page;
            response.data = res.data.data;

            
        })
        .catch((err) => 
        {
            console.log(err);
        });
    }
    return response;

}