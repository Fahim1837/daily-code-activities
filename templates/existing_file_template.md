<div style="display: flex; justify-content: space-between; align-items:end;">
  <div style="display:flex">
      <img src="../assets/branch.svg" alt="GitHub Logo"  style="width:20px; margin:0 10px 0 0">
      <h3 style="margin: 0; padding:0; font-weight: bold; font-size:20px;">{{ current_branch }}</h3>
  </div>
  <div style="display:flex">
  {% if server_name == 'github' %}<img src="../assets/github.svg" alt="GitHub Logo" style="width:20px">
    {% elif server_name == 'aws' %}<img src="../assets/amazon.svg" alt="Amazon Logo" style="width:20px">
    {% endif %}<span style="color:rgb(16, 54, 226); text-align: right; margin:0 0 0 10px; padding:0px;">{{ date }}, {{ year }} | {{ time }}</span>
  </div>
</div>

**_Commit:_** <code style="color: red; font-weight: bold;">{{ commit_id }}</code>
**Message:** {{ commit_message }}
**Description:**
- {{ commit_description }}
---