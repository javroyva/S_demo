# -*- coding: utf-8 -*

__copyright__       = "Copyright 2020 Cells-IA www.cells-ia.com"

import os
import sys
import json
import logging
import shutil
from shapely.geometry import box

import cytomine
from cytomine.models import JobData
from cytomine.models import Annotation, AnnotationTerm, AnnotationCollection
from cytomine.models import ProjectCollection, Project, PropertyCollection, Property
from cytomine.models import ImageInstanceCollection, ImageInstance
from cytomine.models import OntologyCollection, Ontology, TermCollection, Term
from cytomine.models import StorageCollection, Storage

#Connection to Cytomine Core
__credentials_file__ = "credentials_ht.json"
__username__ = 'admin'

def run(cyto_job, parameters):

    logging.info("----- test software v%s -----", __version__)
    logging.info("Entering run(cyto_job=%s, parameters=%s)", cyto_job, parameters)

    job = cyto_job.job
    project = cyto_job.project

    ontologies = OntologyCollection().fetch()
    ontology = next(o for o in ontologies if o.name == 'clinic_ontology_AI')
    terms = TermCollection().fetch_with_filter('ontology',ontology.id)

    new_project = Project(name = parameters.project_name)
    new_project.save()


    # images = ImageInstanceCollection().fetch_with_filter('project', project.id)
    # for image in images:
    #     annotations = AnnotationCollection()
    #     annotations.project = project.id
    #     annotations.fetch()
    #     nb_annotations = len(annotations)
    #     progress = 0
    #     progress_delta = 100 / nb_annotations
    #     for i,annotation in enumerate(annotations):
    #         annotation.fetch()
        
    #         try:
    #             job.update(progress=progress, statusComment="Generating annotation {} of {}...".format(i,nb_annotations))
    #             Annotation(location=annotation.location, id_image = image.id, id_terms=annotation.term, id_project = project.id).save()
    #             annotation.detete()
    #             progress += progress_delta
    #         except:
    #             logging.info("Error al crear nueva anotación")

if __name__ == "__main__":
    logging.debug("Command: %s", sys.argv)

    with cytomine.CytomineJob.from_cli(sys.argv) as cyto_job:
        run(cyto_job, cyto_job.parameters)