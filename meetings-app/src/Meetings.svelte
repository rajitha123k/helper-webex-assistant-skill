<script>
  import { Router, Route, Link, navigate} from 'svelte-routing';
  import { onMount } from 'svelte';
  import { Client } from "@microsoft/microsoft-graph-client";

  const API_KEY = process.env.GOOGLE_API_KEY
  const DISCOVERY_DOCS = ['https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest'];
  const SCOPES = 'https://www.googleapis.com/auth/calendar.readonly';
  const CLIENT_ID = process.env.PUBLIC_GOOGLE_CLIENT_ID
  let msalInstance;

  let events = [];
  const start = async () => {
    await loadClient();
    await authorize();
  };
  const provider  = localStorage.getItem("provider")
  function initialize() {
    const provider  = localStorage.getItem("provider")
    if (provider === "Google") {
      gapi?.load('client', start);
    }
  }

  onMount(async () => {
		const provider  = localStorage.getItem("provider")
    if (provider === "Microsoft") {
      try {
        const graphClient = Client.init({
          authProvider: async (done) => {
            done(null, localStorage.getItem('access_token'));
          },
        });
  
        const msevents = await graphClient.api('/me/calendar/events')
          .filter(`start/dateTime ge '${new Date().toISOString()}'`)
          .select('subject,start,end')
          .orderby('start/dateTime')
          .get();
        
        events =  msevents?.value?.map((event) => {
          return {
            title: event.subject,
            start: event.start.dateTime,
            end: event.end.dateTime,
          };
        })?? [];
      } catch (error) {
        console.log('Error during login:', error);
      }
    }
  });

  function loadClient() {
    window.gapi.load("client:auth2", initClient);
  }

  const openSignInPopup = () => {
    window.gapi.auth2.authorize(
      { client_id: CLIENT_ID, scope: SCOPES },
      (res) => {
        if (res) {
          console.log("🚀 ~ file: Meetings.svelte:67 ~ openSignInPopup ~ res:", res);
          if (res.access_token)
            localStorage.setItem("access_token", res.access_token);
          window.gapi.client.load("calendar", "v3", listUpcomingEvents);
        }
      }
    );
} 


const fetchEvents = () => {
  // Get events if access token is found without sign in popup
  fetch(`https://www.googleapis.com/calendar/v3/calendars/primary/events?key=${API_KEY}&orderBy=startTime&singleEvents=true&timeMin=${new Date().toISOString()}&maxResults=10`,
    {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("access_token")}`,
      },
    }
  )
    .then((res) => {
      if (res.status !== 401) {
        return res.json();
      } else {
        localStorage.removeItem("access_token");
        openSignInPopup();
      }
    })
    .then((data) => {
      if (data?.items) {
        events = formatEvents(data.items)
      }
    });
}
  function initClient() {
    if (!localStorage.getItem("access_token")) {
      openSignInPopup();
    } else {
      fetchEvents();
    }
  };
  function authorize() {
    return window.gapi.client
      .init({
        clientId: CLIENT_ID,
        apiKey: API_KEY,
        scope: SCOPES,
        discoveryDocs: DISCOVERY_DOCS,
        plugin_name: 'meetingapp'
      })
  }

  function listUpcomingEvents() {
    fetchEvents();
  }

  const formatEvents = (list) => {
    return list.map((item) => ({
      title: item.summary,
      start: item.start.dateTime,
      end: item.end.dateTime,
    }));
  };

  async function getOutlookMeetings() {
    try {
      const response = await client.api('/me/events')
        .filter("start/dateTime ge '2023-06-16T00:00:00'")
        .select('subject,start,end')
        .orderby('start/dateTime')
        .get();

      const meetings = response.value;
      console.log('Outlook Meetings:');
      meetings.forEach((meeting) => {
        console.log(`- Subject: ${meeting.subject}`);
        console.log(`  Start: ${meeting.start.dateTime}`);
        console.log(`  End: ${meeting.end.dateTime}`);
      });
    } catch (error) {
      console.log(`Error retrieving Outlook meetings: ${error}`);
    }
  }

  function logout() {
  window.gapi.auth2.getAuthInstance().signOut();
  localStorage.removeItem("access_token");
  console.log("🚀 ~ file: Login.svelte:51 ~ logout ~ logout:", 'logout');
  navigate("/login", { replace: true });
}
</script>

<div>
  <div class="topnav">
  <h1>{provider} Upcoming Events</h1>
  <button on:click={() => logout()}>Logout</button>
</div>
  {#if events.length === 0}
    <p>No {provider} upcoming events.</p>
  {:else}
    <ul>
      {#each events as event}
        <li key={event.id}>
          <h3>{event.title}</h3>
          <p>Starts: {event.start}</p>
          <p>Ends: {event.end}</p>
        </li>
      {/each}
    </ul>
  {/if}
</div>

<style>
  .topnav {
  background-color: #333;
  overflow: hidden;
}

/* Style the links inside the navigation bar */
.topnav h1 {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 30px;
}

/* Change the color of links on hover */
.topnav button {
  background-color: #ddd;
  color: black;
  float: right;
  padding: 14px 16px;
  margin-right:30px;
  margin-top:30px;
}

/* Add a color to the active/current link */
.topnav a.active {
  background-color: #04AA6D;
  color: white;
}
</style>

<svelte:head>
  <script src="https://apis.google.com/js/api.js" on:load={initialize}></script>
</svelte:head>
