import VueJwtDecode from 'vue-jwt-decode';

const decodeToken = (token) => {
    try{
      return VueJwtDecode.decode(token)

    }
    catch(error){
      console.log('Token Error: ', error);
      return null

    }
}

export default decodeToken
