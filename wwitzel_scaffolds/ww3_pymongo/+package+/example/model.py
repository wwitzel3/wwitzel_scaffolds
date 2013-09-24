def get_example(request):
    return request.db.example.find_one({'name':request.matchdict['name']})

