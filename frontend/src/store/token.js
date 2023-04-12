import jwt_decode from "jwt-decode";

const decodeToken = (token) => {
  console.log("decodeToken")
    try {
      return jwt_decode(token)

    }
    catch(error) {
      console.log('Token Error: ', error);
      return null

    }
}

export const populateStore = (state, token) => {
  state.isAuthenticated = true

  const decoded = decodeToken(token)

  state.username = decoded['username']
  state.first_name = decoded['first_name']
  state.last_name = decoded['last_name']
  state.email = decoded['email']
  state.institution = decoded['institution']
  state.experience = decoded['experience']
  state.approved = decoded['approved']
}

export const depopulateStore = (state) => {
  state.isAuthenticated = false

  state.username = ''
  state.first_name = ''
  state.last_name = ''
  state.email = ''
  state.institution = ''
  state.experience = ''
  state.approved = ''
}
