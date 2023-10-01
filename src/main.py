import openai
from .utils import get_static_file, throw_if_missing
import os

def eatUser(user_data):
    return user_data

def handlePrompt(prompt,context):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=int(os.environ.get("OPENAI_MAX_TOKENS", "512")),
            messages=[{"role": "user", "content": context.req.body["prompt"]}],
        )
        completion = response.choices[0].message.content
        json_data= {"ok": True, "completion": completion}
        return json_data
    except Exception:
        json_error = {"ok": False, "error": "Failed to query model."}
        return json_error

def main(context):
    throw_if_missing(os.environ, ["OPENAI_API_KEY"])

    if context.req.method == "GET":
        return context.res.send(
            get_static_file("index.html"),
            200,
            {
                "content-type": "text/html",
            },
        )

    req_body = context.req.body
    command = req_body["cmd"]
    cmd_data = re_body["content"]

    if commmand == "eat_mem" :
        prompt_dta = handlePrompt(cmd_data,context)
        if prompt_dta["ok"]==True:
            return context.res.json(prompt_dta, 200)
        else:
            return context.res.json(prompt_dta, 500)
    elif command == "eat_user":
            usr_data = eatUser(cmd_data)
            return context.res.json(usr_dta, 200)
    #try:
    #    throw_if_missing(context.req.body, ["prompt"])
    #except ValueError as err:
    #    return context.res.json({"ok": False, "error": err.message}, 400)

    #openai.api_key = os.environ["OPENAI_API_KEY"]

    #try:
        
    #    response = openai.ChatCompletion.create(
    #        model="gpt-3.5-turbo",
    #        max_tokens=int(os.environ.get("OPENAI_MAX_TOKENS", "512")),
    #        messages=[{"role": "user", "content": context.req.body["prompt"]}],
    #    )
    #    completion = response.choices[0].message.content
    #    return context.res.json({"ok": True, "completion": completion}, 200)

    #except Exception:
    #   return context.res.json({"ok": False, "error": "Failed to query model."}, 500)
