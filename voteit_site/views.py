from arche.views.base import BaseView
from arche.interfaces import IDocument
from arche.interfaces import IBlobs
from arche import security


class DocumentView(BaseView):

    def __call__(self):
        return {'has_image': 'image' in IBlobs(self.context)}


def includeme(config):
    config.add_view(DocumentView,
                    name = "view",
                    context = IDocument,
                    permission = security.PERM_VIEW,
                    renderer = "templates/document.pt")
