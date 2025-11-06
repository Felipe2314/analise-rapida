from django.db import models


class SoftDeleteQuerySet(models.QuerySet):
    """QuerySet com suporte a Soft Delete"""

    def delete(self):
        """Soft delete em massa"""
        return super().update(is_active=False)

    def hard_delete(self):
        """Exclusão real em massa"""
        return super().delete()

    def restore(self):
        """Restaura registros 'apagados'"""
        return super().update(is_active=True)


class SoftDeleteManager(models.Manager):
    """Manager que retorna apenas objetos ativos"""
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).filter(is_active=True)


class AllObjectsManager(models.Manager):
    """Manager que retorna todos os objetos, inclusive deletados"""
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db)
