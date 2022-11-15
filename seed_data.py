from errno import EADDRNOTAVAIL
from mailbox import NoSuchMailboxError
from ejemplo.models import Familiar

Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()


print("Se cargo con éxito los usuarios de pruebas")

from blog.models import Post

Post(title="Mi post", short_content="un post", content="sadljalsjdlkajsdljasljdlaksjd").save()

print("Se cargo con éxito los post de pruebas")