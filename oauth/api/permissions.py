from rest_framework import permissions

class IsAuthenticatedOrCreated(permissions.IsAuthenticated):
    def has_permissions(self,request,view):
        if request.method == 'POST':
            return True
        return super(IsAuthenticatedOrCreated,self).has_permissions(request,view)
        