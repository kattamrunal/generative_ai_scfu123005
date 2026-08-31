# EX 3- Meeting transcript to action items pipeline
# build a 3 step pipeline. Step 1: extracts what was discussed from a raw meeting transcript 
# Step 2: identifies action items from that discussion , flagging anything where an owner or deadline is missing
# Step 3: formats the fimal list into structured task table
# input : transcript_text
# output :discussion summary from step 1, the flagged action items from step 2 and final structed task table from step 3 

import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  # API KEY HERE
)

transcript_text = """
Alice: We discussed launching the new website next month.
Bob: I'll handle the homepage redesign.
Alice: Great. Can you finish it by September 10?
Bob: Yes.

Charlie: We also need to prepare the marketing campaign.
Alice: Someone should create the social media assets.
Charlie: I'll look into it.

Bob: We should review the project budget.
Alice: Yes, let's get that done soon.
"""
# step 1: extract wt was discussed

step1_prompt=f"""
You are analyzing a meeting transcript.

Extract and summarize ONLY what was discussed in the meeting.

Group the discussion into clear topics.
Do not invent information.

Meeting transcript:{transcript_text}
"""
step1 = client.chat.completions.create(
  model="nvidia/nemotron-3-ultra-550b-a55b",
  messages=[{"role":"user","content":step1_prompt}],
  temperature=1,
  top_p=0.95,
  max_tokens=16384,
  extra_body={"chat_template_kwargs":{"enable_thinking":True}},

)

discussion_summary = step1.choices[0].message.content

# step 2: identify action items

step2_prompt=f"""You are identifying action items from a meeting discussion.

For every action item:
- Identify the task
- Identify the owner if explicitly mentioned
- Identify the deadline if explicitly mentioned
- If the owner is missing, flag it as "MISSING OWNER"
- If the deadline is missing, flag it as "MISSING DEADLINE"
- Do not infer an owner or deadline
- Do not create action items that were not discussed

Discussion_summary:{discussion_summary}
"""

step2=client.chat.completions.create(
  model="nvidia/nemotron-3-ultra-550b-a55b",
  messages=[{"role":"user","content":step2_prompt}],
  temperature=1,
  top_p=0.95,
  max_tokens=16384,
  extra_body={"chat_template_kwargs":{"enable_thinking":True}},

)

action_items=step2.choices[0].message.content

# step 3: formating into strucured task table

step3_prompt = f"""
Convert the following action items into a structured task table.

Use exactly these columns:

| Task | Owner | Deadline | Status/Flags |

Rules:
- Preserve the information from the action items.
- Do not invent missing information.
- Use "Not specified" when an owner or deadline is missing.
- Put "MISSING OWNER" and/or "MISSING DEADLINE" in Status/Flags.
- Keep each action item as a separate row.

Action items:
{action_items}
"""
step3=client.chat.completions.create(
  model="nvidia/nemotron-3-ultra-550b-a55b",
  messages=[{"role":"user","content":step3_prompt}],
  temperature=1,
  top_p=0.95,
  max_tokens=16384,
  extra_body={"chat_template_kwargs":{"enable_thinking":True}},

)

final_task_table = step3.choices[0].message.content

print("\n========== STEP 1: DISCUSSION SUMMARY ==========\n")
print(discussion_summary)

print("\n========== STEP 2: FLAGGED ACTION ITEMS ==========\n")
print(action_items)

print("\n========== STEP 3: FINAL STRUCTURED TASK TABLE ==========\n")
print(final_task_table)
