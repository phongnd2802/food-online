from django.core.exceptions import PermissionDenied

def detect_user(user):
    if user.role == 1:
        redirect_url = 'vendor-dashboard'
    elif user.role == 2:
        redirect_url = 'cust-dashboard'
    elif user.role is None and user.is_superadmin:
        redirect_url = '/admin'
    return redirect_url

def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied
    
def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied