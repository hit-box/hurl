from app import app


@app.route("/predicate/error/type")
def predicate_error_type():
    return """{
     "status": true, 
     "message": "0", 
     "count": 1, 
     "empty": "", 
     "number": 1.0,
     "list": [1,2,3],
     "not_a_date": "2018",
     "is_a_date": "2018-12-10T13:45:00.000Z",
     "ipv4": "127.0.0.1",
     "ipv6": "2001:db8::1"
}"""
