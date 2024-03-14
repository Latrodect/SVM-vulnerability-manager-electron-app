import axios from './AxiosInterceptor'

const BASE_URL = ''
const END_POINT = ''
class SignInService{
    
     SignInPostRequest(body){
        const config = {
            headers: {
              "Content-Type": "application/json",
            },
          };
        return axios.post(`${BASE_URL}/${END_POINT}`, JSON.stringify(body), config=config)
    }
}
export default new SignInService();
