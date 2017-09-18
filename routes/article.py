from . import template, login_required
from sanic import Blueprint

bp = Blueprint('article', url_prefix='/articles')


@bp.route('/')
async def index(request):
    return template('article/index.html')


@bp.route('/<id:int>', methods=['GET'])
async def detail(request, id):
    return template('article/detail.html', id=id)


@bp.route('/new', methods=['GET'])
@login_required
async def new(request):
    return template('article/new.html')


@bp.route('/category/<category:str>', methods=['GET'])
async def new(request, category):
    return template('article/new.html')
