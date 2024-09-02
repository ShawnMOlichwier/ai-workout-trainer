# ai-workout-trainer


Awesome resource to get started with free API access
https://github.com/cheahjs/free-llm-api-resources

* Thinking Groq right now 1440 requests per day seems decent for my use case



# Active todo:
- [ ] Get V0.1 of the app working in streamlit with chat
    - [ ] formatted output properly with editable table

- Install Docker locally to build app image
- Get pathing working properly in app script
- Update the prompt for proper formatting
    - Add a finish for workouts :]
- Add format to st.dataframe.  
    - Make it editable
- Connect Linux machine to NAS
    - Setup and connect to postgres DB
- Self-host langfuse


# Initial ideas 
* Consider wrapping everything in Langfuse
    * https://langfuse.com/

* We need chat history to update our workout list before we get started
    * Take in previous workout and modify with the given user's update
    * How do we handle this with the client?
        * If first query, do generate()
        * else, do update_response()
        * Have a counter to keep track of this? 
        * Or can we just throw it all in the chat history and have the LLM figure it out, probably tbh

* Front end to display generated workouts

* Prompt to give upper body, lower, core, etc. These can came from buttons in the app

* Motivational quote to accompany workout

* Prompt formatting for correct output
    * Agnetic framework to find videos and explain moves from youtube

* Gather knowledge base of workouts

* Host on NAS

* Built in rep counter

* Create mobile app

* Save / export / import workouts from previous sessions
    * Save to local backend database on NAS

* Have backlog of workouts to call to
    * Inject into prompt to help standardize workouts
    * This needs clarified. It all depends on how well the LLM performs without existing workouts to work off
    * The LLM might do well enough from just the knowledge base and itself

* High temperature for variability of workouts


* As a side note, this could also apply to BJJ
    * I want to drill guard passing today, what should I work on
    * Could use metadata for inside or outside passing