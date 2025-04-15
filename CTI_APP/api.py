from ninja import Router
from .schema import *
from .models import CtiLog, BlackListIP, BlackListURL


router = Router()


@router.get("/black-list-url", response=list[BlackListURLOut])
def get_black_list_url(request):
    return BlackListURL.objects.all()


@router.post("/black-list-url-create", response=BlackListURLOut)
def post_black_list_url(request, body: BlackListURLPost):
    black_url = BlackListURL.objects.create(**body.dict())
    return black_url


@router.get("/black-list-ip/", response=list[BlackListIPOut])
def get_blacklist(request):
    return BlackListIP.objects.all()

@router.post("/black-list-ip-create/", response=BlackListIPOut)
def create_blacklist_entry(request, data: BlackListIPIn):
    entry = BlackListIP.objects.create(**data.dict())
    return entry


@router.get('/threat-list', response=list[CtiOutSchema])
def get_cti_list(request):
    queryset = CtiLog.objects.all()
    return queryset


@router.post('/threat-create', response=CtiOutSchema)
def post_cti(request, data: CtiPostSchema):
    cti = CtiLog.objects.create(**data.dict())
    return cti