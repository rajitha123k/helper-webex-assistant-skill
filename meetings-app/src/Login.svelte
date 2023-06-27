<script>
  import { Router, Route, Link, navigate} from 'svelte-routing';
  import { PublicClientApplication, EventType } from '@azure/msal-browser';
  import { onMount } from 'svelte';

  const SCOPES = 'https://www.googleapis.com/auth/calendar.readonly';
	const CLIENT_ID = process.env.PUBLIC_GOOGLE_CLIENT_ID
  let msalInstance;
  const MS_clientId = process.env.MS_clientId;
  console.log("MS_clientId", MS_clientId)
  const MS_redirectUri = process.env.MS_redirectUri;

  onMount(() => {
    console.log("MS_clientId1", MS_clientId)
    msalInstance = new PublicClientApplication({
      auth: {
        clientId: MS_clientId,
        redirectUri: MS_redirectUri,
      },
      cache: {
        cacheLocation: 'localStorage',
        storeAuthStateInCookie: true,
      },
    });

    msalInstance.addEventCallback((event) => {
      if (event.eventType === EventType.LOGIN_SUCCESS && event.payload.account) {
        // alert('Login successful!');
        // console.log('Access token:', event.payload.accessToken);
        // localStorage.setItem('access_token', event.payload.accessToken);
        // navigate("/meetings", { replace: true });
      }
    });
  });

  async function handleLogin(provider) {
    localStorage.setItem('provider', provider);
    if (provider == 'Google') {
      window.gapi.load("client:auth2", openSignInPopup);
    } else if (provider == 'Microsoft') {
      try {
        const loginRequest = {
          scopes: ['User.Read', 'Calendars.Read'],
        };
        const loginResponse = await msalInstance.loginPopup(loginRequest);
        console.log('Login response:', loginResponse);
        localStorage.setItem('access_token', loginResponse.accessToken);
        navigate("/meetings", { replace: true });
      } catch (error) {
        console.log('Error during login:', error);
      }
    }
  }

  const openSignInPopup = () => {
    window.gapi.auth2.authorize(
      { client_id: CLIENT_ID, scope: SCOPES },
      (res) => {
        if (res) {
          if (res.access_token)
            localStorage.setItem("access_token", res.access_token);
          navigate("/meetings", { replace: true });
        }
      }
  );
} 
function logout() {
  window.gapi.auth2.getAuthInstance().signOut();
  localStorage.removeItem("access_token");
  console.log("🚀 ~ file: Login.svelte:51 ~ logout ~ logout:", 'logout');
}
</script>

<main>
  <!-- <button on:click={() => logout()}>logout</button> -->
  <h1>Login</h1>
  <button on:click={() => handleLogin('Google')}>Login with Google</button>
  <button on:click={() => handleLogin('Microsoft')}>Login with Microsoft</button>
</main>
<svelte:head>
  <script src="https://apis.google.com/js/api.js"></script>
</svelte:head>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }

  h1 {
    margin-bottom: 1rem;
  }

  button {
    margin-bottom: 0.5rem;
  }
</style>