snek_object_t *snek_add(snek_object_t *a, snek_object_t *b) {
  if (a == NULL || b == NULL) {
    return NULL;
  }

  switch (a->kind) {
  case INTEGER:
    switch (b->kind) {
    case INTEGER:
      return new_snek_integer(a->data.v_int + b->data.v_int);
    case FLOAT:
      return new_snek_float((float)a->data.v_int + b->data.v_float);
    default:
      return NULL;
    }
  case FLOAT:
    switch (b->kind) {
    case FLOAT:
      return new_snek_float(a->data.v_float + b->data.v_float);
    default:
      return snek_add(b, a);
    }
  case STRING:
    switch (b->kind) {
    case STRING: {
      int a_len = strlen(a->data.v_string);
      int b_len = strlen(b->data.v_string);
      int len = a_len + b_len + 1;
      char *dst = calloc(len, sizeof(char));

      strcat(dst, a->data.v_string);
      strcat(dst, b->data.v_string);

      snek_object_t *obj = new_snek_string(dst);
      free(dst);

      return obj;
    }
    default:
      return NULL;
    }
  case VECTOR3:
    switch (b->kind) {
    case VECTOR3:
      return new_snek_vector3(
        snek_add(a->data.v_vector3.x, b->data.v_vector3.x),
        snek_add(a->data.v_vector3.y, b->data.v_vector3.y),
        snek_add(a->data.v_vector3.z, b->data.v_vector3.z)
      );
    default:
      return NULL;
    }
  case ARRAY:
    switch (b->kind) {
    case ARRAY: {
      size_t a_len = (size_t)snek_length(a);
      size_t b_len = (size_t)snek_length(b);
      size_t length = a_len + b_len;

      snek_object_t *array = new_snek_array(length);

      for (int i = 0; i <= a_len; i++) {
        snek_array_set(array, i, snek_array_get(a, i));
      }

      for (int i = 0; i <= b_len; i++) {
        snek_array_set(array, i + a_len, snek_array_get(b, i));
      }

      return array;
    }
    default:
      return NULL;
    }
  default:
    return NULL;
  }
}